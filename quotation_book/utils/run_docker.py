import docker


def run_container(cont_name, pwd, port, image_name, detach):
    client = docker.from_env()

    try:
        container = client.containers.run(
            image_name,
            name=cont_name,
            environment={"POSTGRES_PASSWORD": pwd},
            ports={"5432": port},
            detach=detach
        )
        if detach:
            print(f"Container {container.id} started.")
        else:
            print(f"Container not started")
    except docker.errors.ImageNotFound:
        print(f"Image '{image_name}' not found. Please pull the image first.")


if __name__ == "__main__":
    image_name = "postgres"
    cont_name = "hw10"
    pwd = "pass123"
    port = "5432"
    detach = True

    run_container(cont_name, pwd, port, image_name, detach)
