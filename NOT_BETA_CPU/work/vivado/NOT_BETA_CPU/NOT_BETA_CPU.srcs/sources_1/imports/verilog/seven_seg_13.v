/*
   This file was generated automatically by Alchitry Labs version 1.2.7.
   Do not edit this file directly. Instead edit the original Lucid source.
   This is a temporary file and any changes made to it will be destroyed.
*/

module seven_seg_13 (
    input [3:0] char,
    output reg [6:0] segs
  );
  
  
  
  always @* begin
    
    case (char)
      4'h0: begin
        segs = 7'h3f;
      end
      4'h1: begin
        segs = 7'h06;
      end
      4'h2: begin
        segs = 7'h5b;
      end
      4'h3: begin
        segs = 7'h4f;
      end
      4'h4: begin
        segs = 7'h66;
      end
      4'h5: begin
        segs = 7'h6d;
      end
      4'h6: begin
        segs = 7'h7d;
      end
      4'h7: begin
        segs = 7'h07;
      end
      4'h8: begin
        segs = 7'h7f;
      end
      4'h9: begin
        segs = 7'h67;
      end
      4'ha: begin
        segs = 7'h77;
      end
      4'hb: begin
        segs = 7'h7c;
      end
      4'hc: begin
        segs = 7'h39;
      end
      4'hd: begin
        segs = 7'h5e;
      end
      4'he: begin
        segs = 7'h79;
      end
      4'hf: begin
        segs = 7'h71;
      end
      default: begin
        segs = 7'h00;
      end
    endcase
  end
endmodule
