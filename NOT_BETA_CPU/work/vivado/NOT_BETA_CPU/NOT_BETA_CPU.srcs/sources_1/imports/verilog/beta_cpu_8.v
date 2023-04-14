/*
   This file was generated automatically by Alchitry Labs version 1.2.7.
   Do not edit this file directly. Instead edit the original Lucid source.
   This is a temporary file and any changes made to it will be destroyed.
*/

module beta_cpu_8 (
    input clk,
    input slowclk,
    input rst,
    input [31:0] instruction,
    output reg [31:0] ia,
    output reg [63:0] debug,
    output reg led_matrix_output,
    output reg [1:0] led_current_player,
    input [4:0] playerButtoninput,
    input valid_led_on,
    input buzzer_on,
    input reset_signal,
    output reg [7:0] led_player_timer,
    output reg [63:0] debug_reg_content,
    input [3:0] debug_register_index,
    output reg buzzer_output
  );
  
  
  
  wire [3-1:0] M_control_system_pcsel;
  wire [1-1:0] M_control_system_asel;
  wire [1-1:0] M_control_system_ra2sel;
  wire [1-1:0] M_control_system_bsel;
  wire [6-1:0] M_control_system_alufn;
  wire [2-1:0] M_control_system_wdsel;
  wire [1-1:0] M_control_system_werf;
  reg [1-1:0] M_control_system_z;
  reg [6-1:0] M_control_system_opcode;
  control_unit_17 control_system (
    .z(M_control_system_z),
    .opcode(M_control_system_opcode),
    .pcsel(M_control_system_pcsel),
    .asel(M_control_system_asel),
    .ra2sel(M_control_system_ra2sel),
    .bsel(M_control_system_bsel),
    .alufn(M_control_system_alufn),
    .wdsel(M_control_system_wdsel),
    .werf(M_control_system_werf)
  );
  
  wire [64-1:0] M_alu_system_out;
  wire [3-1:0] M_alu_system_zvn;
  reg [64-1:0] M_alu_system_a;
  reg [64-1:0] M_alu_system_b;
  reg [6-1:0] M_alu_system_alufn_signal;
  alu_18 alu_system (
    .a(M_alu_system_a),
    .b(M_alu_system_b),
    .alufn_signal(M_alu_system_alufn_signal),
    .out(M_alu_system_out),
    .zvn(M_alu_system_zvn)
  );
  
  wire [1-1:0] M_regfile_system_z;
  wire [64-1:0] M_regfile_system_reg_data_1;
  wire [64-1:0] M_regfile_system_reg_data_2;
  wire [256-1:0] M_regfile_system_grid;
  wire [2-1:0] M_regfile_system_current_player;
  wire [8-1:0] M_regfile_system_current_timer;
  wire [64-1:0] M_regfile_system_debug_reg_content;
  reg [4-1:0] M_regfile_system_ra;
  reg [4-1:0] M_regfile_system_rb;
  reg [4-1:0] M_regfile_system_rc;
  reg [1-1:0] M_regfile_system_werf;
  reg [64-1:0] M_regfile_system_wdsel_out;
  reg [1-1:0] M_regfile_system_slowclk;
  reg [4-1:0] M_regfile_system_debug_register_index;
  regfile_unit_19 regfile_system (
    .clk(clk),
    .rst(rst),
    .ra(M_regfile_system_ra),
    .rb(M_regfile_system_rb),
    .rc(M_regfile_system_rc),
    .werf(M_regfile_system_werf),
    .wdsel_out(M_regfile_system_wdsel_out),
    .slowclk(M_regfile_system_slowclk),
    .debug_register_index(M_regfile_system_debug_register_index),
    .z(M_regfile_system_z),
    .reg_data_1(M_regfile_system_reg_data_1),
    .reg_data_2(M_regfile_system_reg_data_2),
    .grid(M_regfile_system_grid),
    .current_player(M_regfile_system_current_player),
    .current_timer(M_regfile_system_current_timer),
    .debug_reg_content(M_regfile_system_debug_reg_content)
  );
  
  wire [32-1:0] M_pc_system_pc_4;
  wire [32-1:0] M_pc_system_pc_4_sxtc;
  wire [32-1:0] M_pc_system_pcsel_out;
  wire [32-1:0] M_pc_system_ia;
  reg [1-1:0] M_pc_system_slowclk;
  reg [18-1:0] M_pc_system_id;
  reg [3-1:0] M_pc_system_pcsel;
  reg [64-1:0] M_pc_system_reg_data_1;
  reg [1-1:0] M_pc_system_reset_signal;
  pc_unit_20 pc_system (
    .clk(clk),
    .rst(rst),
    .slowclk(M_pc_system_slowclk),
    .id(M_pc_system_id),
    .pcsel(M_pc_system_pcsel),
    .reg_data_1(M_pc_system_reg_data_1),
    .reset_signal(M_pc_system_reset_signal),
    .pc_4(M_pc_system_pc_4),
    .pc_4_sxtc(M_pc_system_pc_4_sxtc),
    .pcsel_out(M_pc_system_pcsel_out),
    .ia(M_pc_system_ia)
  );
  
  wire [3-1:0] M_buttonHandler_out;
  reg [5-1:0] M_buttonHandler_player_button;
  player_button_handler_21 buttonHandler (
    .player_button(M_buttonHandler_player_button),
    .out(M_buttonHandler_out)
  );
  
  wire [1-1:0] M_outputHandler_outled;
  wire [2-1:0] M_outputHandler_current_player_LED_sig;
  wire [1-1:0] M_outputHandler_buzzer_output;
  reg [256-1:0] M_outputHandler_grid;
  reg [2-1:0] M_outputHandler_current_player;
  reg [1-1:0] M_outputHandler_valid_led_on;
  reg [1-1:0] M_outputHandler_buzzer_on;
  output_handler_22 outputHandler (
    .clk(clk),
    .rst(rst),
    .grid(M_outputHandler_grid),
    .current_player(M_outputHandler_current_player),
    .valid_led_on(M_outputHandler_valid_led_on),
    .buzzer_on(M_outputHandler_buzzer_on),
    .outled(M_outputHandler_outled),
    .current_player_LED_sig(M_outputHandler_current_player_LED_sig),
    .buzzer_output(M_outputHandler_buzzer_output)
  );
  
  reg [2:0] M_player_button_buffer_d, M_player_button_buffer_q = 1'h0;
  
  reg M_reset_button_buffer_d, M_reset_button_buffer_q = 1'h0;
  
  reg [63:0] bsel_out;
  
  reg [63:0] wdsel_out;
  
  always @* begin
    M_reset_button_buffer_d = M_reset_button_buffer_q;
    M_player_button_buffer_d = M_player_button_buffer_q;
    
    ia = 1'h0;
    debug = 64'h0000000000000000;
    M_control_system_opcode = 1'h0;
    M_control_system_z = 1'h0;
    M_regfile_system_ra = 1'h0;
    M_regfile_system_rb = 1'h0;
    M_regfile_system_rc = 1'h0;
    M_regfile_system_werf = 1'h0;
    M_regfile_system_slowclk = 1'h0;
    M_pc_system_slowclk = 1'h0;
    M_pc_system_id = 1'h0;
    M_pc_system_reg_data_1 = 1'h0;
    M_pc_system_pcsel = 1'h0;
    M_buttonHandler_player_button = playerButtoninput;
    M_player_button_buffer_d = M_buttonHandler_out;
    if (M_player_button_buffer_q != 1'h0) begin
      M_player_button_buffer_d = M_player_button_buffer_q;
    end
    M_outputHandler_grid = M_regfile_system_grid;
    led_matrix_output = M_outputHandler_outled;
    M_outputHandler_current_player = M_regfile_system_current_player;
    led_current_player = M_outputHandler_current_player_LED_sig;
    M_outputHandler_valid_led_on = valid_led_on;
    M_outputHandler_buzzer_on = buzzer_on;
    buzzer_output = M_outputHandler_buzzer_output;
    led_player_timer = M_regfile_system_current_timer;
    M_alu_system_alufn_signal = M_control_system_alufn;
    
    case (M_control_system_bsel)
      1'h0: begin
        bsel_out = M_regfile_system_reg_data_2;
      end
      1'h1: begin
        bsel_out = instruction[0+17-:18];
      end
      default: begin
        bsel_out = M_regfile_system_reg_data_2;
      end
    endcase
    
    case (M_control_system_wdsel)
      2'h0: begin
        wdsel_out = M_pc_system_pc_4;
      end
      2'h1: begin
        wdsel_out = M_alu_system_out;
      end
      2'h3: begin
        wdsel_out = M_player_button_buffer_q;
        if (slowclk) begin
          M_player_button_buffer_d = 1'h0;
        end
      end
      default: begin
        wdsel_out = M_alu_system_out;
      end
    endcase
    M_alu_system_a = M_regfile_system_reg_data_1;
    M_alu_system_b = bsel_out;
    M_regfile_system_wdsel_out = wdsel_out;
    M_control_system_opcode = instruction[26+5-:6];
    M_control_system_z = M_regfile_system_z;
    M_pc_system_slowclk = slowclk;
    M_pc_system_reg_data_1 = M_regfile_system_reg_data_1;
    M_pc_system_pcsel = M_control_system_pcsel;
    M_pc_system_id = instruction[0+17-:18];
    ia = M_pc_system_ia;
    M_pc_system_reset_signal = M_reset_button_buffer_q;
    M_reset_button_buffer_d = reset_signal;
    if (M_reset_button_buffer_q != 1'h0) begin
      M_reset_button_buffer_d = M_reset_button_buffer_q;
    end
    if (slowclk) begin
      if (M_reset_button_buffer_q != 1'h0) begin
        M_reset_button_buffer_d = 1'h0;
      end
    end
    M_regfile_system_slowclk = slowclk;
    M_regfile_system_werf = M_control_system_werf;
    M_regfile_system_ra = instruction[18+3-:4];
    M_regfile_system_rb = instruction[14+3-:4];
    M_regfile_system_rc = instruction[22+3-:4];
    debug[0+0+15-:16] = M_pc_system_pc_4_sxtc[0+15-:16];
    debug[32+0+15-:16] = bsel_out[0+15-:16];
    debug[48+0+15-:16] = wdsel_out[0+15-:16];
    debug_reg_content = M_regfile_system_debug_reg_content;
    M_regfile_system_debug_register_index = debug_register_index;
  end
  
  always @(posedge clk) begin
    if (rst == 1'b1) begin
      M_reset_button_buffer_q <= 1'h0;
    end else begin
      M_reset_button_buffer_q <= M_reset_button_buffer_d;
    end
  end
  
  
  always @(posedge clk) begin
    if (rst == 1'b1) begin
      M_player_button_buffer_q <= 1'h0;
    end else begin
      M_player_button_buffer_q <= M_player_button_buffer_d;
    end
  end
  
endmodule
