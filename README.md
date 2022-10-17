# python-bazel-docker-app

To run the app with Bazel:

```bash
bazel run //app/app

# Same as
# bazel run //app/app:app
```

To build the Docker image with Bazel:

```bash
bazel build //app/app:image
```

To run the Docker image locally:

```bash
bazel run //app/app:image
docker run --rm bazel/app/app:image
```

To inspect the Docker image:

```bash
bazel run //app/app:image
docker run --rm -it --entrypoint /bin/sh bazel/app/app:image
```
