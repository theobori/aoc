{
  pkgs,
  lib,
  stdenvNoCC,
  python3,
  writeShellApplication,
}:
let
  supportedPythonRuntimes = with pkgs; [
    pypy
    (python3.withPackages (p: [
      p.numpy
      p.shapely
    ]))
  ];
in
stdenvNoCC.mkDerivation (finalAttrs: {
  pname = "x";
  version = "0.0.1";

  dontUnpack = true;

  nativeBuildInputs = with pkgs; [
    makeWrapper
  ];

  installPhase = ''
    runHook preInstall

    mkdir -p $out/{bin,share/x}

    cp ${./x.py} "$out/share/x/x.py"

    makeWrapper ${python3.interpreter} "$out/bin/x" \
      --add-flags "$out/share/x/x.py" \
      --prefix PATH : ${lib.makeBinPath supportedPythonRuntimes}

    runHook postInstall
  '';

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
              text = ''${finalAttrs.finalPackage}/bin/x ${year} ${problem} ${part} "$@"'';
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
})
