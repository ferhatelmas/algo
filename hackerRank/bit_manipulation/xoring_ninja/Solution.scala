package bit_manipulation.xoring_ninja

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val lines = Source.stdin.getLines.drop(1)
    while(lines.hasNext) {
      val (n, mod) = (BigInt(2).pow(lines.next.toInt - 1), BigInt(1000000007))
      println((n * lines
        .next
        .split("\\s")
        .map(_.toInt)
        .fold(0)((a, b) => a | b)) % mod)
    }
  }
}
