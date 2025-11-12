import time

# --- Subsystems ---
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

# client code without facade

# Client manually controls every step
vcs = VersionControlSystem()
build = BuildSystem()
test = TestSystem()
deploy = DeploymentSystem()

vcs.pull_latest_changes("main")
build.compile_project()
test.run_tests()
deploy.deploy()


# ❌ Problem

# The client knows too much about internal systems.

# Every subsystem’s method order, naming, and timing must be managed manually.

# If one subsystem changes, all clients must update their code.

# ================================================
# solution with Facade Pattern

# We introduce a Facade class that hides the complexity behind one simple interface.

# 🧠 Concept

# The Facade Pattern provides a unified, simplified interface to a complex subsystem.

# So instead of calling 4–5 classes, the client just calls one method like:
    
#     pipeline.deploy_application("main")
