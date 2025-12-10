{
  pkgs,
  lib,
  python3,
  writeShellApplication,
  buildPythonApplication,

  # Python build time
  setuptools,

  # Python run time
  numpy,
  shapely,
  loguru,
  pydantic,
}:
let
  # For static derivations only
  supportedPythonRuntimes = with pkgs; [
    pypy
    (python3.withPackages (p: [
      p.numpy
      p.shapely
    ]))
  ];
  self = buildPythonApplication {
    pname = "x";
    version = "0.0.1";
    pyproject = true;

    src = ./.;

    build-system = [
      setuptools
    ];

    dependencies = [
      numpy
      shapely
      loguru
      pydantic
    ];

    pythonImportsCheck = [ "x" ];

    passthru =
      let
        years = {
          "2023" = 25;
          "2024" = 25;
          "2025" = 12;
        };

        parts = {
          "1" = 1;
          "2" = 2;
        };

        inherit (lib.lists) range;
        inherit (lib) listToAttrs pathExists;
      in
      builtins.mapAttrs (
        year: problemsAmount:
        let
          problems' = range 1 problemsAmount;
          problems = listToAttrs (
            builtins.map (problem: {
              name = builtins.toString problem;
              value = problem;
            }) problems'
          );
        in
        builtins.mapAttrs (
          problemName: problemValue:
          builtins.mapAttrs (
            part: _:
            let
              problem = if problemValue < 10 then "0" + problemName else problemName;
              scriptNameSuffix = "${year}-${problem}-${part}";
            in
            rec {
              dynamic = writeShellApplication {
                name = "dynamic-${scriptNameSuffix}";
                text = ''${self}/bin/x run ${year} ${problem} ${part} "$@"'';
              };

              static =
                let
                  solutionPath = ./${year}/${problem}/part${part}.py;
                in
                if pathExists solutionPath then
                  writeShellApplication {
                    name = "static-${scriptNameSuffix}";
                    text = ''${solutionPath} "$@"'';
                    runtimeInputs = supportedPythonRuntimes;
                  }
                else
                  dynamic;
            }
          ) parts
        ) problems
      ) years;

    meta = {
      mainProgram = "x";
    };
  };
in
self
