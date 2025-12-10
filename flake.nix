{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    treefmt-nix.url = "github:numtide/treefmt-nix";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      treefmt-nix,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        treefmtEval = treefmt-nix.lib.evalModule pkgs ./treefmt.nix;
        aoc-solutions = pkgs.callPackage ./default.nix {
          inherit (pkgs.python3Packages)
            buildPythonApplication
            setuptools
            numpy
            shapely
            loguru
            pydantic
            ;
        };
      in
      {
        packages = {
          default = aoc-solutions;
          inherit aoc-solutions;
        };

        devShells = {
          default = pkgs.mkShell {
            venvDir = ".venv";
            packages =
              with pkgs;
              [
                # Keep in this order
                pypy
                python3
              ]
              ++ (with pkgs.python3Packages; [
                pip
                venvShellHook
                setuptools
                # GNU Emacs Python LSP installed within the virtual environment
                # otherwise my LSP installed outside could not reach the venv packages.
                # See https://github.com/emacs-lsp/lsp-mode/issues/393
                python-lsp-server
              ])
              ++ aoc-solutions.dependencies;
          };
        };

        formatter = treefmtEval.config.build.wrapper;

        checks = {
          formatting = treefmtEval.config.build.check self;
        };
      }
    );
}
