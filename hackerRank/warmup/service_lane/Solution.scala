package warmup.service_lane

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val lines = Source.stdin.getLines.drop(1)
    val ls = lines.next.split("\\s").map(_.toInt)
    for(ln <- lines) {
      val Array(i, j) = ln.split("\\s").map(_.toInt)
      println(ls.drop(i).take(j-i+1).min)
    }
  }
}
