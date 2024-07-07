{ pkgs }: {
  env = "python";
  packages = with pkgs.pythonPackages; [ flask flask_restful flask-cors requests ];
}

