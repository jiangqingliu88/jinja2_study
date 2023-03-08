#表示函数执行成功返回 0
cd units/wrf/sim
make uvm TEST=wrf_smoke_tet>gate.log
if
grep "TEST PASSED" gate.log
then
    echo "pass"
    exit
else
    echo "FAil"
    exit 1
fi
rm -rf gate.log