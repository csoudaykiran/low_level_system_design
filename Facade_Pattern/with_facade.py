import time

# --- Subsystems (same as before) ---
class VersionControlSystem:
    def pull_latest_changes(self, branch):
        print(f"VCS: Pulling latest changes from '{branch}'...")
        time.sleep(1)
        print("VCS: Pull complete.")

class BuildSystem:
    def compile_project(self):
        print("BuildSystem: Compiling project...")
        time.sleep(1)
        print("BuildSystem: Build successful.")

class TestSystem:
    def run_tests(self):
        print("TestSystem: Running tests...")
        time.sleep(1)
        print("TestSystem: All tests passed.")

class DeploymentSystem:
    def deploy(self):
        print("DeploymentSystem: Deploying to server...")
        time.sleep(1)
        print("DeploymentSystem: Deployment successful!")

# --- Facade ---
class DevOpsFacade:
    def __init__(self):
        self.vcs = VersionControlSystem()
        self.builder = BuildSystem()
        self.tester = TestSystem()
        self.deployer = DeploymentSystem()

    def deploy_application(self, branch):
        print("\n🚀 Starting Deployment Pipeline...")
        self.vcs.pull_latest_changes(branch)
        self.builder.compile_project()
        self.tester.run_tests()
        self.deployer.deploy()
        print("✅ Deployment pipeline completed successfully!\n")




# Client only interacts with the Facade
pipeline = DevOpsFacade()
pipeline.deploy_application("main")
