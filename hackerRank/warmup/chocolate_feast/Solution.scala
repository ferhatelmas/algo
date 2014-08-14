package warmup.chocolate_feast

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(ln <- Source.stdin.getLines.drop(1)) {
      val Array(n, c, k) = ln.split("\\s").map(_.toInt)
      def wrap(m: Int): Int = if(m < k) 0 else m / k + wrap(m % k + m / k)
      println(n / c + wrap(n / c))
    }
  }
}
