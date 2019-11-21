
import java.util.*;

class Solution {
    public String solution(String sentence) {
        String answer = "";
        if(sentence.split(" ").length != 1) return "invalid";
        List<Character> wordList = new ArrayList<>();

        while(sentence.length() > 0) {
            if('a' <= sentence.charAt(0) && sentence.charAt(0) <= 'z') {
                if(wordList.contains(sentence.charAt(0))) {
                    return "invalid";
                }

                wordList.add(sentence.charAt(0));
                String[] sentenceFormat = rule2(sentence);
                if(sentenceFormat[0].equals("invalid")) {
                    return sentenceFormat[0];
                }
                sentence = sentence.replaceFirst(sentenceFormat[1], "");
                if(sentence.length() == 0) {
                    answer = answer + sentenceFormat[0];
                } else {
                    answer = answer + sentenceFormat[0] + " ";
                }
            } else {
                if(sentence.length() > 1 && 'a' <= sentence.charAt(1) && sentence.charAt(1) <= 'z') {
                    if(wordList.contains(sentence.charAt(1))) {
                        return "invalid";
                    }
                    wordList.add(sentence.charAt(1));
                }
                String[] sentenceFormat = rule1(sentence);
                if(sentenceFormat[0].equals("invalid")) {
                    return sentenceFormat[0];
                }
                sentence = sentence.replaceFirst(sentenceFormat[1], "");
                if(sentence.length() == 0) {
                    answer = answer + sentenceFormat[0];
                } else {
                    answer = answer + sentenceFormat[0] + " ";
                }
            }
        }
        return answer;
    }

    public String[] rule1(String sentence) {
        String w = "";
        int i;
        char sta_word;
        if(sentence.length() > 1)
            sta_word = sentence.charAt(1);
        else
            return new String[] {sentence, sentence};

        for(i = 0; i < sentence.length(); i++) {
            char word = sentence.charAt(i);

            if(i % 2 == 0) {
                if('A' <= word && word <= 'Z') {
                    w = w + word;
                } else {
                    return new String[] {"invalid"};
                }
            } else {
                if('a' <= word && word <= 'z') {
                    if(sta_word != word) break;
                } else {
                    break;
                }
            }
        }
        return new String[] {w, sentence.substring(0, i)};
    }

    public String[] rule2(String sentence) {
        char sta_word = sentence.charAt(0);
        int i = 1;
        while(i < sentence.length()) {
            char word = sentence.charAt(i);
            if(sta_word == word) {
                return new String[] {sentence.substring(1, i), sentence.substring(0, i+1)};
            } else if ('a' <= word && word <= 'z' && word != sta_word) {
                String[] sentenceFormat = rule1(sentence.substring(i - 1, sentence.length()));
                if(sentenceFormat[0].equals("invalid")) {
                    return new String[] {"invalid"};
                } else {
                    
                }
            }
            i++;
        }

        return new String[] {"invalid"};
    }

    public static void main(String[] args) {
        Solution so = new Solution();
        System.out.println(so.solution("HaEaLaLObWORLDb"));
    }
  }