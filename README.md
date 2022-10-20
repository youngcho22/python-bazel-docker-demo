# python-bazel-docker-app

To run the app with Bazel:

```bash
bazel run //fibonacci:app
```

To run all tests with Bazel:

```bash
bazel test //...
```

To build the Docker image with Bazel:

```bash
bazel build //fibonacci:image
```

To run the Docker image locally:

```bash
bazel run //fibonacci:image
docker run --rm bazel/fibonacci:image
```

To inspect the Docker image:

```bash
bazel run //app/app:image
docker run --rm -it --entrypoint /bin/sh bazel/fibonacci:image
```
