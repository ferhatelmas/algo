package project_euler.q2_even_fibonacci_numbers

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    lazy val fibs: Stream[BigInt] = BigInt(1) #:: BigInt(2) #:: fibs.zip(
      fibs.tail).map { t =>
      t._1 + t._2
    }
    for(n <- Source.stdin.getLines.drop(1).map(BigInt(_))) {
      println(fibs.takeWhile(_ <= n).filter(_ % 2 == 0).sum)
    }
  }
}
