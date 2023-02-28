(ns day-7
  (:require [instaparse.core :as insta]
            [clojure.string :as str]
            [clojure.core.match :refer [match]]))

(def parse-line
  (insta/parser
    "line = command-line | ls-result-line
     ls-result-line = word <' '+> word
     command-line = <'$'> <' '+> command [<' '+> arguments]
     command = 'ls' | 'cd'
     arguments = #'[a-zA-Z0-9/.]+'
     word = #'[a-zA-Z0-9.]+'
    "))

(defn get-line-type
  [parsed-line]
  (get-in parsed-line [1 0]))

(defn get-command
  [parsed-line]
  (get-in parsed-line [1 1 1]))

(defn get-arguments
  [parsed-line]
  (get-in parsed-line [1 2 1]))

(defn get-file-size
  [parsed-line]
  (get-in parsed-line [1 1 1]))

(defn get-file-name
  [parsed-line]
  (get-in parsed-line [1 2 1]))

(def sample-data-ls
  [:line [:command-line [:command "ls"]]])

(def sample-data-cd
  [:line [:command-line [:command "cd"] [:arguments ".."]]])

(def sample-data-file
  [:line [:ls-result-line [:word "62596"] [:word "h.lst"]]])

(def sample-state
  {:current-dir "/home/thanh/"
   :file-sizes  {}})

(defn prev-dir
  [current-dir]
  (if (= current-dir "/")
    "/"
    (as-> current-dir _
          (str/split _ #"/")
          (drop-last _)
          (str/join "/" _)
          (str _ "/"))))

(defn chdir
  [current-dir path]
  (cond (= path "..") (prev-dir current-dir)
        (str/starts-with? path "/") path
        :else (str current-dir path "/")))

(defn apply-cd
  [state parsed-line]
  (let [current-dir (get state :current-dir)
        folder-name (get-arguments parsed-line)
        new-dir (chdir current-dir folder-name)]
    (assoc state :current-dir new-dir)
    ))

(defn apply-ls-result
  [state parsed-line]
  (let [file-name (get-file-name parsed-line)
        file-size (get-file-size parsed-line)
        file-path (-> state
                      (get :current-dir)
                      (str file-name)
                      (keyword))]
    (assoc-in state [:file-sizes file-path] file-size)))

(defn apply-line
  [state parsed-line]
  (let [line-type (get-line-type parsed-line)
        command (get-command parsed-line)
        file-size (get-file-size parsed-line)]
    (match [line-type command file-size]
           [:command-line "ls" _] state
           [:command-line "cd" _] (apply-cd state parsed-line)
           [:ls-result-line _ "dir"] state
           [:ls-result-line _ _] (apply-ls-result state parsed-line)
           :else (throw (ex-info "day-7.apply-line unreachable path"
                                 {:state       state
                                  :parsed-line parsed-line}))
           )))

(defn get-parent-dirs
  "Get parent directories from a file's full path"
  [path]
  (->> (str/split path #"/")
       (reductions conj [])
       (drop 1)
       (drop-last 1)
       (map #(str/join "/" %))
       (map #(str % "/"))
       ))

(get-parent-dirs "/home/thanh/a.xyz")

(apply-ls-result sample-state [:line [:ls-result-line [:word "62596"] [:word "h.lst"]]])
(apply-cd sample-state [:line [:command-line [:command "cd"] [:arguments ".."]]])
(apply-cd {:current-dir "/home/"} [:line [:command-line [:command "cd"] [:arguments ".."]]])
(apply-line {:current-dir "/home/" :file-sizes {}} [:line [:command-line [:command "cd"] [:arguments ".."]]])
(apply-line {:current-dir "/home/" :file-sizes {}} [:line [:ls-result-line [:word "62596"] [:word "h.lst"]]])
(apply-line {:current-dir "/home/" :file-sizes {}} [:line [:command-line [:command "cd"] [:arguments "tab"]]])

(parse-line "dir d")

(let [parsed-lines (->> (slurp "inputs/day_7.txt")
                        (str/trim-newline)
                        (str/split-lines)
                        (map parse-line))
      initial-state {:current-dir "/"
                     :file-sizes  {}}
      final-state (reduce apply-line initial-state parsed-lines)
      folder-sizes (->> (get final-state :file-sizes)
                        (map (fn [[key value]]
                               (let [keys (get-parent-dirs (str key))]
                                 (map (fn [sub-key]
                                        [sub-key value])
                                      keys))))
                        (apply concat)
                        (map (fn [[key value]] [key (Integer/parseInt value)]))
                        (group-by first)
                        (map (fn [[key kvs]] [key (map second kvs)]))
                        (map (fn [[key vals]] [key (reduce + vals)]))
                        (into {}))
      total-size-available 70000000
      total-size-used (get folder-sizes ":/")
      total-size-unused (- total-size-available total-size-used)
      total-size-required (- 30000000 total-size-unused)

      part-1-answer (->> folder-sizes
                         (filter (fn [[folder total]] (< total 100000)))
                         (map second)
                         (reduce +))
      part-2-answer (->> folder-sizes
                         (filter (fn [[folder total]] (> total total-size-required)))
                         (map second)
                         (sort)
                         (first))
      ]
  part-2-answer)
