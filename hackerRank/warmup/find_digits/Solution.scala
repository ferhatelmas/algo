package warmup.find_digits

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(s <- Source.stdin.getLines.drop(1)) {
      val i = s.toInt
      println(s.map(c => if(c != '0' && i % (c - '0') == 0) 1 else 0).sum)
    }
  }
}
