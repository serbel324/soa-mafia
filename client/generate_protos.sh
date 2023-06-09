src=../common/protos
out=.
# rm $out/*.py 2>/dev/null
python -m grpc_tools.protoc -I$src --python_out=$out --pyi_out=$out --grpc_python_out=$out $src/*.proto