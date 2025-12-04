{
  pkgs,
  lib,
  stdenvNoCC,
  python3,
  writeShellScriptBin,
}:
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
      --add-flags "$out/share/x/x.py"

    runHook postInstall
  '';

  passthru = builtins.mapAttrs (
    year: problemsAmount:
    let
      problems' = range 1 problemsAmount;
      problems = listToAttrs (
        builtins.map (problem: {
          "name" = builtins.toString problem;
          "value" = problem;
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
          path = ./${year}/${problem}/part${part}.py;
        in
        rec {
          dynamic = writeShellScriptBin "dynamic-${scriptNameSuffix}" "${finalAttrs.finalPackage}/bin/x ${year} ${problem} ${part} $@";
          static =
            if pathExists path then
              (writeShellScriptBin "static-${scriptNameSuffix}" "${path} $@")
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
