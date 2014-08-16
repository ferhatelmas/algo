package math.reverse_game

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(List(n, k) <- Source.stdin.getLines.drop(1).map(_.split("\\s").map(_.toInt).toList)) {
      var i = k
      for(j <- 0 until n if i >= j) {
        i = n - 1 - i + j
      }
      println(i)
    }
  }
}
