# python-bazel-docker-demo

To run the app with Bazel:

```bash
bazel run //app
```

To build the Docker image with Bazel:

```bash
bazel build //app:image
```

To run the Docker image locally:

```bash
bazel run //app:image
docker run --rm bazel/app:image
```

To inspect the Docker image:

```bash
bazel run //app:image
docker run --rm -it --entrypoint /bin/sh bazel/app:image
```
