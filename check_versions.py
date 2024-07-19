import pkg_resources

def get_installed_packages():
    installed_packages = pkg_resources.working_set
    packages = [(pkg.project_name, pkg.version) for pkg in installed_packages]
    return packages

if __name__ == "__main__":
    packages = get_installed_packages()
    for name, version in packages:
        print(f"{name}=={version}")