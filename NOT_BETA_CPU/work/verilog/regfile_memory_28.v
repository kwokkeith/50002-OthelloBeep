/*
   This file was generated automatically by Alchitry Labs version 1.2.7.
   Do not edit this file directly. Instead edit the original Lucid source.
   This is a temporary file and any changes made to it will be destroyed.
*/

module regfile_memory_28 (
    input clk,
    input rst,
    input [3:0] read_address_1,
    input [3:0] read_address_2,
    output reg [63:0] reg_data_1,
    output reg [63:0] reg_data_2,
    input [3:0] write_address,
    input [63:0] write_data,
    input write_enable,
    output reg [255:0] grid,
    output reg [1:0] current_player,
    output reg [7:0] current_timer,
    input [3:0] debug_register_index,
    output reg [63:0] debug_register_output
  );
  
  
  
  reg [1023:0] M_registers_d, M_registers_q = 1024'h0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000;
  
  always @* begin
    M_registers_d = M_registers_q;
    
    reg_data_1 = 1'h0;
    reg_data_2 = 1'h0;
    reg_data_1 = M_registers_q[(read_address_1)*64+63-:64];
    reg_data_2 = M_registers_q[(read_address_2)*64+63-:64];
    if (write_address != 4'hf && write_enable) begin
      M_registers_d[(write_address)*64+63-:64] = write_data;
    end
    if (read_address_1 == 4'hf) begin
      reg_data_1 = 64'h0000000000000000;
    end
    if (read_address_2 == 4'hf) begin
      reg_data_2 = 64'h0000000000000000;
    end
    grid[0+63-:64] = {M_registers_q[704+56+7-:8], M_registers_q[704+48+0-:1], M_registers_q[704+49+0-:1], M_registers_q[704+50+0-:1], M_registers_q[704+51+0-:1], M_registers_q[704+52+0-:1], M_registers_q[704+53+0-:1], M_registers_q[704+54+0-:1], M_registers_q[704+55+0-:1], M_registers_q[704+40+7-:8], M_registers_q[704+32+0-:1], M_registers_q[704+33+0-:1], M_registers_q[704+34+0-:1], M_registers_q[704+35+0-:1], M_registers_q[704+36+0-:1], M_registers_q[704+37+0-:1], M_registers_q[704+38+0-:1], M_registers_q[704+39+0-:1], M_registers_q[704+24+7-:8], M_registers_q[704+16+0-:1], M_registers_q[704+17+0-:1], M_registers_q[704+18+0-:1], M_registers_q[704+19+0-:1], M_registers_q[704+20+0-:1], M_registers_q[704+21+0-:1], M_registers_q[704+22+0-:1], M_registers_q[704+23+0-:1], M_registers_q[704+8+7-:8], M_registers_q[704+0+0-:1], M_registers_q[704+1+0-:1], M_registers_q[704+2+0-:1], M_registers_q[704+3+0-:1], M_registers_q[704+4+0-:1], M_registers_q[704+5+0-:1], M_registers_q[704+6+0-:1], M_registers_q[704+7+0-:1]};
    grid[64+63-:64] = {M_registers_q[640+56+7-:8], M_registers_q[640+48+0-:1], M_registers_q[640+49+0-:1], M_registers_q[640+50+0-:1], M_registers_q[640+51+0-:1], M_registers_q[640+52+0-:1], M_registers_q[640+53+0-:1], M_registers_q[640+54+0-:1], M_registers_q[640+55+0-:1], M_registers_q[640+40+7-:8], M_registers_q[640+32+0-:1], M_registers_q[640+33+0-:1], M_registers_q[640+34+0-:1], M_registers_q[640+35+0-:1], M_registers_q[640+36+0-:1], M_registers_q[640+37+0-:1], M_registers_q[640+38+0-:1], M_registers_q[640+39+0-:1], M_registers_q[640+24+7-:8], M_registers_q[640+16+0-:1], M_registers_q[640+17+0-:1], M_registers_q[640+18+0-:1], M_registers_q[640+19+0-:1], M_registers_q[640+20+0-:1], M_registers_q[640+21+0-:1], M_registers_q[640+22+0-:1], M_registers_q[640+23+0-:1], M_registers_q[640+8+7-:8], M_registers_q[640+0+0-:1], M_registers_q[640+1+0-:1], M_registers_q[640+2+0-:1], M_registers_q[640+3+0-:1], M_registers_q[640+4+0-:1], M_registers_q[640+5+0-:1], M_registers_q[640+6+0-:1], M_registers_q[640+7+0-:1]};
    grid[128+63-:64] = {M_registers_q[576+56+7-:8], M_registers_q[576+48+0-:1], M_registers_q[576+49+0-:1], M_registers_q[576+50+0-:1], M_registers_q[576+51+0-:1], M_registers_q[576+52+0-:1], M_registers_q[576+53+0-:1], M_registers_q[576+54+0-:1], M_registers_q[576+55+0-:1], M_registers_q[576+40+7-:8], M_registers_q[576+32+0-:1], M_registers_q[576+33+0-:1], M_registers_q[576+34+0-:1], M_registers_q[576+35+0-:1], M_registers_q[576+36+0-:1], M_registers_q[576+37+0-:1], M_registers_q[576+38+0-:1], M_registers_q[576+39+0-:1], M_registers_q[576+24+7-:8], M_registers_q[576+16+0-:1], M_registers_q[576+17+0-:1], M_registers_q[576+18+0-:1], M_registers_q[576+19+0-:1], M_registers_q[576+20+0-:1], M_registers_q[576+21+0-:1], M_registers_q[576+22+0-:1], M_registers_q[576+23+0-:1], M_registers_q[576+8+7-:8], M_registers_q[576+0+0-:1], M_registers_q[576+1+0-:1], M_registers_q[576+2+0-:1], M_registers_q[576+3+0-:1], M_registers_q[576+4+0-:1], M_registers_q[576+5+0-:1], M_registers_q[576+6+0-:1], M_registers_q[576+7+0-:1]};
    grid[192+63-:64] = {M_registers_q[384+56+7-:8], M_registers_q[384+48+0-:1], M_registers_q[384+49+0-:1], M_registers_q[384+50+0-:1], M_registers_q[384+51+0-:1], M_registers_q[384+52+0-:1], M_registers_q[384+53+0-:1], M_registers_q[384+54+0-:1], M_registers_q[384+55+0-:1], M_registers_q[384+40+7-:8], M_registers_q[384+32+0-:1], M_registers_q[384+33+0-:1], M_registers_q[384+34+0-:1], M_registers_q[384+35+0-:1], M_registers_q[384+36+0-:1], M_registers_q[384+37+0-:1], M_registers_q[384+38+0-:1], M_registers_q[384+39+0-:1], M_registers_q[384+24+7-:8], M_registers_q[384+16+0-:1], M_registers_q[384+17+0-:1], M_registers_q[384+18+0-:1], M_registers_q[384+19+0-:1], M_registers_q[384+20+0-:1], M_registers_q[384+21+0-:1], M_registers_q[384+22+0-:1], M_registers_q[384+23+0-:1], M_registers_q[384+8+7-:8], M_registers_q[384+0+0-:1], M_registers_q[384+1+0-:1], M_registers_q[384+2+0-:1], M_registers_q[384+3+0-:1], M_registers_q[384+4+0-:1], M_registers_q[384+5+0-:1], M_registers_q[384+6+0-:1], M_registers_q[384+7+0-:1]};
    current_player = M_registers_q[256+0+1-:2];
    current_timer = M_registers_q[512+0+7-:8];
    debug_register_output = M_registers_q[(debug_register_index)*64+63-:64];
  end
  
  always @(posedge clk) begin
    if (rst == 1'b1) begin
      M_registers_q <= 1024'h0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000;
    end else begin
      M_registers_q <= M_registers_d;
    end
  end
  
endmodule