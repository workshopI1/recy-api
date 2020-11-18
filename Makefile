deps:
	python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-2.3.0-cp38-cp38-macosx_10_14_x86_64.whl

build:
	docker build -t zhuharev/waste-detection-server .

push:
	docker push zhuharev/waste-detection-server

run:
	docker run -it --rm -p 8080:8080 zhuharev/waste-detection-server