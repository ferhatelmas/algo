package warmup.the_love_letter_mystery

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(s <- Source.stdin.getLines.drop(1)) {
      val l = s.length
      println((for(i <- 0 until l / 2) yield Math.abs(s.charAt(i) - s.charAt(l-i-1))).sum)
    }
  }
}

