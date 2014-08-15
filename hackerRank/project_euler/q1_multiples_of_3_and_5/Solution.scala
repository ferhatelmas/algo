package project_euler.q1_multiples_of_3_and_5

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    def sum(n: Long): Long = n * (n+1) / 2
    for(n <- Source.stdin.getLines.drop(1).map(_.toInt)) {
      val List(k3, k5, k15) = List(3L, 5L, 15L).map(i => i * sum((n-1)/i)).toList
      println(k3 + k5 - k15)
    }
  }
}
