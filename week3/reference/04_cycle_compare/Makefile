SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Reuse mac.v from 3-2 reference — student demonstrably uses cumulative RTL artifact
VERILOG_SOURCES = $(PWD)/../02_mac_verilog/mac.v
TOPLEVEL = mac
MODULE = test_cycle_compare

include $(shell cocotb-config --makefiles)/Makefile.sim
