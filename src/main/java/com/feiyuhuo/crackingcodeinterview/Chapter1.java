package com.feiyuhuo.crackingcodeinterview;

/**
 * Created by ourstart on 16/11/15.
 */
public class Chapter1 {

    public static boolean isUniqChars2(String str) {
        boolean[] char_set = new boolean[256];
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (char_set[val]) {
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }



    public static void main(String[] args) {
        System.out.println(isUniqChars2("abc"));
    }
}
