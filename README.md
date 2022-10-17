# python-bazel-docker-demo

To run the app with Bazel:

```bash
bazel run //demo/app

# Same as
# bazel run //demo/app:app
```

To build the Docker image with Bazel:

```bash
bazel build //demo/app:image
```

To run the Docker image locally:

```bash
bazel run //demo/app:image
docker run --rm bazel/demo/app:image
```

To inspect the Docker image:

```bash
bazel run //demo/app:image
docker run --rm -it --entrypoint /bin/sh bazel/demo/app:image
```
