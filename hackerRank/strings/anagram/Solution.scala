package strings.anagram

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(ln <- Source.stdin.getLines.drop(1)) {
      val l = ln.length
      println(
        if(l % 2 == 1) -1
        else ln.substring(0, l/2).sorted.diff(ln.substring(l/2)).length
      )
    }
  }
}
