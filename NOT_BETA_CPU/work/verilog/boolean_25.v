/*
   This file was generated automatically by Alchitry Labs version 1.2.7.
   Do not edit this file directly. Instead edit the original Lucid source.
   This is a temporary file and any changes made to it will be destroyed.
*/

module boolean_25 (
    input [63:0] a,
    input [63:0] b,
    input [5:0] alufn_signal,
    output reg [63:0] out
  );
  
  
  
  always @* begin
    
    case (alufn_signal[0+3-:4])
      4'h8: begin
        out = a & b;
      end
      4'he: begin
        out = a | b;
      end
      4'h6: begin
        out = a ^ b;
      end
      4'ha: begin
        out = a;
      end
      default: begin
        out = 64'h0000000000000000;
      end
    endcase
  end
endmodule