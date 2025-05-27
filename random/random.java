import java.util.Random;

public class Random128Bit {
    public static void main(String[] args) {
        Random random = new Random();
        byte[] bytes = new byte[16]; // 16 bytes = 128 bits
        random.nextBytes(bytes);

        // Print as binary string
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0'));
        }
        System.out.println(sb.toString()); // 128-bit binary sequence
    }
}