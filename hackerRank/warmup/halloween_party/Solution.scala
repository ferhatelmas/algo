package warmup.halloween_party

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(ln <- Source.stdin.getLines.drop(1)) {
      val i = ln.toLong
      println((i/2) * (i/2 + i%2))
    }
  }
}
