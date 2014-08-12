package warmup.manasa_and_stones

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(ns <- Source.stdin.getLines.drop(1).grouped(3).map(_.map(_.toInt))) {
      println(
        (for(i <- 0 until ns(0) by 1)
          yield ns(1) * i + ns(2) * (ns(0)-i-1)
        ).toSet.toList.sorted.mkString(" "))
    }
  }
}
