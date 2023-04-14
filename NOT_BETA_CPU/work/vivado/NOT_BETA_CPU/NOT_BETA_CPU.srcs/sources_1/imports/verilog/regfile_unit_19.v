/*
   This file was generated automatically by Alchitry Labs version 1.2.7.
   Do not edit this file directly. Instead edit the original Lucid source.
   This is a temporary file and any changes made to it will be destroyed.
*/

module regfile_unit_19 (
    input clk,
    input rst,
    input [3:0] ra,
    input [3:0] rb,
    input [3:0] rc,
    input werf,
    input [63:0] wdsel_out,
    input slowclk,
    output reg z,
    output reg [63:0] reg_data_1,
    output reg [63:0] reg_data_2,
    output reg [255:0] grid,
    output reg [1:0] current_player,
    output reg [7:0] current_timer,
    input [3:0] debug_register_index,
    output reg [63:0] debug_reg_content
  );
  
  
  
  wire [64-1:0] M_regfile_reg_data_1;
  wire [64-1:0] M_regfile_reg_data_2;
  wire [256-1:0] M_regfile_grid;
  wire [2-1:0] M_regfile_current_player;
  wire [8-1:0] M_regfile_current_timer;
  wire [64-1:0] M_regfile_debug_register_output;
  reg [4-1:0] M_regfile_read_address_1;
  reg [4-1:0] M_regfile_read_address_2;
  reg [4-1:0] M_regfile_write_address;
  reg [64-1:0] M_regfile_write_data;
  reg [1-1:0] M_regfile_write_enable;
  reg [4-1:0] M_regfile_debug_register_index;
  regfile_memory_28 regfile (
    .clk(clk),
    .rst(rst),
    .read_address_1(M_regfile_read_address_1),
    .read_address_2(M_regfile_read_address_2),
    .write_address(M_regfile_write_address),
    .write_data(M_regfile_write_data),
    .write_enable(M_regfile_write_enable),
    .debug_register_index(M_regfile_debug_register_index),
    .reg_data_1(M_regfile_reg_data_1),
    .reg_data_2(M_regfile_reg_data_2),
    .grid(M_regfile_grid),
    .current_player(M_regfile_current_player),
    .current_timer(M_regfile_current_timer),
    .debug_register_output(M_regfile_debug_register_output)
  );
  
  reg [3:0] ra2sel_out;
  
  always @* begin
    ra2sel_out = 1'h0;
    z = 1'h0;
    M_regfile_write_enable = 1'h0;
    if (slowclk) begin
      M_regfile_write_enable = werf;
    end
    M_regfile_read_address_2 = rb;
    M_regfile_read_address_1 = ra;
    M_regfile_write_address = rc;
    M_regfile_write_data = wdsel_out;
    z = ~(|M_regfile_reg_data_1);
    reg_data_1 = M_regfile_reg_data_1;
    reg_data_2 = M_regfile_reg_data_2;
    grid = M_regfile_grid;
    current_player = M_regfile_current_player;
    current_timer = M_regfile_current_timer;
    M_regfile_debug_register_index = debug_register_index;
    debug_reg_content = M_regfile_debug_register_output;
  end
endmodule
