package math.stepping_stones_game

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(n <- Source.stdin.getLines.drop(1).map(_.toLong)) {
      val i = (Math.sqrt(1 + 8*n) - 1) / 2
      if(i - i.toLong < 0.000001)
        println("Go On Bob " + i.toLong)
      else
        println("Better Luck Next Time")
    }
  }
}
