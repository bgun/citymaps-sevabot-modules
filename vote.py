#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A voting module
"""

import os
import sys
import random
import sqlite3

conn = sqlite3.connect("vote.db", isolation_level=None)
conn.row_factory = sqlite3.Row

class Answer:
    def __init__(self, data):
        self.id = data["id"]
        self.question_id = data["question_id"]
        self.answer = data["answer"]
        self.qindex = data["qindex"]

    def save(self):
        stmt = conn.cursor()

        if self.id == None:
            stmt.execute("INSERT INTO answer "
                         "(question_id, answer, qindex) VALUES "
                         "(?, ?, ?)",
                         (self.question_id, self.answer, self.qindex))
            self.id = stmt.lastrowid
        else:
            stmt.execute("UPDATE answer SET "
                         "question_id = ?,"
                         "answer = ?,"
                         "qindex = ? "
                         "WHERE id = ?",
                         (self.question_id, self.answer, self.qindex, self.id))

    @staticmethod
    def getForQuestion(id):
        stmt = conn.cursor()
        stmt.execute("SELECT * FROM answer WHERE question_id = " + id)

        answers = []
        rows = stmt.fetchall()

        for row in rows:
            answers.append(Answer(row))

        return answers



    @staticmethod
    def createTableIfNeeded():
        stmt = conn.cursor()
        stmt.execute("CREATE TABLE IF NOT EXISTS answer ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "answer TEXT,"
                     "qindex INTEGER,"
                     "question_id INTEGER"
                     ")")
    @staticmethod
    def reset():
        stmt = conn.cursor()
        stmt.execute("DELETE FROM answer")

Answer.createTableIfNeeded()


class Question:
    def __init__(self, data, answers = None):
        self.id = data["id"]
        self.question = data["question"]
        self.active = data["active"]
        self.creator = data["creator"]

        if answers != None:
            self.answers = answers
        else:
            self.answers = []

    def addAnswer(self, text):
        self.answers.append(Answer({
            "id" : None,
            "answer" : text,
            "qindex" : len(self.answers),
            "question_id" : self.id
        }))

    def save(self):
        stmt = conn.cursor()
        if self.id == None:
            stmt.execute("INSERT INTO question "
                         "(question, active, creator) VALUES "
                         "(?, ?, ?)",
                         [self.question, self.active, self.creator])
            self.id = stmt.lastrowid
        else:
            stmt.execute("UPDATE question SET"
                         "question = ?,"
                         "active = ?,"
                         "creator = ? "
                         "WHERE id = ?",
                         [self.question, self.active, self.creator, self.id])

        for answer in self.answers:
            answer.question_id = self.id
            answer.save()


    @staticmethod
    def getActive():
        stmt = conn.cursor()

        stmt.execute("SELECT * FROM question")
        rows = stmt.fetchall()

        for row in rows:
            answers = Answer.getForQuestion(str(row["id"]))
            question = Question(row, answers)

            return question
        else:
            return None

    @staticmethod
    def createTableIfNeeded():
        stmt = conn.cursor()
        stmt.execute("CREATE TABLE IF NOT EXISTS question ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                     "question TEXT, "
                     "active INTEGER, "
                     "creator TEXT"
                     ")")
    @staticmethod
    def reset():
        stmt = conn.cursor()
        stmt.execute("DELETE FROM question")

Question.createTableIfNeeded()

class Vote:
    def __init__(self, data):
        self.id = data["id"]
        self.question_id = data["question_id"]
        self.answer_id = data["answer_id"]
        self.person = data["person"]

    def save(self):
        stmt = conn.cursor()
        if self.id == None:
            stmt.execute("INSERT INTO vote "
                         "(question_id, answer_id, person) VALUES "
                         "(?, ?, ?)",
                         (self.question_id, self.answer_id, self.person))
            self.id = stmt.lastrowid
        else:
            stmt.execute("UPDATE vote SET "
                         "answer_id = ?,"
                         "question_id = ?,"
                         "person = ?"
                         "WHERE id = ?",
                         (self.answer_id, self.question_id, self.person, self.id))

    @staticmethod
    def getVote(question_id, person):
        stmt = conn.cursor()

        stmt.execute("SELECT * FROM vote WHERE question_id = ? AND person = ?", (question_id, person))

        row = stmt.fetchone()

        if row != None:
            return Vote(row)

        return None

    @staticmethod
    def getVotes(question_id):
        stmt = conn.cursor()

        stmt.execute("SELECT * FROM vote WHERE question_id = ?", [question_id])

        rows = stmt.fetchall()

        votes = []
        for row in rows:
            votes.append(Vote(row))

        return votes

    @staticmethod
    def createTableIfNeeded():
        stmt = conn.cursor()
        stmt.execute("CREATE TABLE IF NOT EXISTS vote ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "question_id INTEGER,"
                     "answer_id INTEGER,"
                     "person TEXT"
                     ")")
    @staticmethod
    def reset():
        stmt = conn.cursor()
        stmt.execute("DELETE FROM vote")

Vote.createTableIfNeeded()

def main(args):
    """The program entry point."""

    random.seed()

    if len(args) <= 0:
        # Roll a six-sided dice
        print random.randint(1, 6)
        return

    cmd = args[0]

    person = os.environ["SKYPE_FULLNAME"]

    admins = ["Ben Gundersen", "Adam Eskreis", "Anthony Campagna"]

    if person in admins:
        admin = True
    else:
        admin = False

    if cmd == 'help':
        print 'Usage:'
        print '       !vote start [question] [answer1] [answer2] ...'
        print '       !vote [answer_num]'
        print '       !vote end'
        return
    elif cmd == 'start':
        question = Question.getActive()

        if question == None:
            question = Question({
                "id" : None,
                "question": args[1],
                "active": str(1),
                "creator": person
            })

            for answer in args[2:]:
                question.addAnswer(answer)

            question.save()

            print "Vote Initiaiated:\n"
        else:
            print "There is already a vote in progress\n"

        print question.question + "\n"

        for answer in question.answers:
            print "Respond !vote " + str(answer.qindex + 1) + " for " + answer.answer

        print "\nVote now!"


        return
    elif cmd == 'end':
        question = Question.getActive()

        if admin or person == question.creator:
            print "Final Results for " + question.question + ":\n"

            votes = Vote.getVotes(question.id)

            answer_counts = [0] * len(question.answers)
            for vote in votes:
                answer_counts[vote.answer_id - 1] += 1

            i = 0
            for answer in question.answers:
                print answer.answer + ": " + str(answer_counts[i]) + " votes"
                i += 1

            Question.reset()
            Answer.reset()
            Vote.reset()
        else:
            print "You are not authorized to end this vote\n"

        return
    else:
        question = Question.getActive()

        try:
            answer_index = int(args[0])

            vote = Vote.getVote(question.id, person)

            if vote == None:
                vote = Vote({
                    "id" : None,
                    "question_id" : question.id,
                    "answer_id" : answer_index,
                    "person" : person
                })
            else:
                vote.answer_id = answer_index;

            vote.save()

            print "Thanks for the vote, " + person + "!"

        except ValueError:
            print "Invalid option chosen\n"

            for answer in question.answers:
                print "Respond !vote " + str(answer.qindex + 1) + " for " + answer.answer

                print "\nVote now!"

        return


if __name__ == '__main__':
    main(sys.argv[1:])
