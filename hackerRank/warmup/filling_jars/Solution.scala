package warmup.filling_jars

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val s = Source.stdin.getLines
    def myToInt(a: String): Array[Long] = a.split("\\s").map(_.toLong)
    val Array(n, _) = myToInt(s.next)
    var sum = 0L
    for(ln <- s) {
      val Array(i, j, k) = myToInt(ln)
      sum += (j-i+1) * k
    }
    println(sum / n)
  }
}
