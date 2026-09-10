"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 07 (i think) OOP main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""
from abc import ABC, abstractmethod
import time
import sys

class StringMatcher(ABC):
    algorithm_name = "Abstract"
    t_complexity = "N/A"
    s_complexity = "N/A"

    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def precomputed_data(self):
        pass

    @abstractmethod
    def precompute(self, pattern):
        pass

    @abstractmethod
    def find_matches(self, text, pattern):
        pass

    def get_report(self, text, pattern):
        start_pre = time.perf_counter()
        self.precompute(pattern)
        pre_time = (time.perf_counter() - start_pre) * 1000

        start_search = time.perf_counter()
        results = self.find_matches(text, pattern)
        search_time = (time.perf_counter() - start_search) * 1000

        return (
            f"--- {self.algorithm_name} ---\n"
            f"Theoretical: {self.t_complexity} Time / {self.s_complexity} Space\n"
            f"Memory Usage: {sys.getsizeof(self.precomputed_data)} bytes\n"
            f"Search Time: {search_time:.4f} ms\n"
            f"Matches: {results}\n"
        )


class KMPMatcher(StringMatcher):
    alorithm_name = "knuth_morris_pratt_match"
    t_complexity = "O(n + m)"
    s_complexity = "O(m)"

    def __init__(self):
        super().__init__()
        self.__lps = [] # private 

    
    @property
    def precomputed_data(self):
        return self.__lps
    
    def precompute(self,pattern): # original LPS from KMP assignment

         self.__lps = [0] * len(pattern)
         length = 0
         i = 1

         while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                self.__lps[i] = length
                i += 1
            else:
                if length == 0:
                    self.__lps[i] = 0
                    i += 1
                else:
                    length = self.__lps[length - 1]

    def find_matches(self, text, pattern): # original match finding for the KMP assignment

        if not pattern or len(pattern) > len(text):
            return []
        
        
        self.precompute(pattern) 

        matches = []
        i = j = 0

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = self.__lps[j - 1]

            if j == len(pattern):
                matches.append(i - j)
                j = self.__lps[j - 1]

        return matches
    

class BruteForceMatcher(StringMatcher):
    alorithm_name = "brute_force_match"
    t_complexity = "O(nm)"
    s_complexity = "O(1)"

    def precompute(self, pattern):
        pass  # nothing to precompute

    @property
    def precomputed_data(self):
        return None

    def find_matches(self, text, pattern): # i made a shortened version of my original code for bruteforce
        if not pattern or len(pattern) > len(text): 
            return []

        matches = []
        n, m = len(text), len(pattern)

        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                matches.append(i)

        return matches



class BoyerMooreMatcher(StringMatcher):
    alorithm_name = "boyer_moore_match"
    t_complexity = "O(n/m)"
    s_complexity = "O( n + \sigma)"

    
    def __init__(self):
        super().__init__()
        self.__bad_char = {}

    def precompute(self, pattern): # original helper function for bad char
        self.__bad_char = {}
        for i in range(len(pattern)):
            self.__bad_char[pattern[i]] = i

    @property
    def precomputed_data(self):
        return self.__bad_char
    
    def find_matches(self, text, pattern): # code from original assignment

        if not pattern or len(pattern) > len(text):
            return []
        
        self.precompute(pattern)

        matches = []
        n, m = len(text), len(pattern)
        shift = 0

        while shift <= n - m:
            j = m - 1

            while j >= 0 and pattern[j] == text[shift + j]:
                j -= 1

            if j < 0:
                matches.append(shift)
                shift += 1
            else:
                bad_char = text[shift + j]
                last = self.__bad_char.get(bad_char, -1)
                shift += max(1, j - last)

        return matches
