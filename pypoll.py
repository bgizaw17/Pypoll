{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-------------------------\n",
      "Election Results\n",
      "-------------------------\n",
      "Total Votes :3521001\n",
      "-------------------------\n",
      "O'Tooley: 2.999999147969569% (105630)\n",
      "Li: 13.999996023857989% (492940)\n",
      "Khan: 63.00001050837531% (2218231)\n",
      "Correy: 19.999994319797125% (704200)\n",
      "-------------------------\n",
      "The winner is: Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "#Set the path for the CSV file\n",
    "\n",
    "PyPollcsv = os.path.join(\"Resources\",\"election_data.csv\")\n",
    "\n",
    "#Create the lists to store data. \n",
    "\n",
    "count = 0\n",
    "candidatelist = []\n",
    "unique_candidate = []\n",
    "vote_count = []\n",
    "vote_percent = []\n",
    "\n",
    "with open(PyPollcsv, newline=\"\") as csvfile:\n",
    "\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "    csv_header = next(csvreader)\n",
    "\n",
    "    # Conduct the ask\n",
    "\n",
    "    for row in csvreader:\n",
    "\n",
    "        #Count the total number of votes\n",
    "\n",
    "        count = count + 1\n",
    "\n",
    "        #Set the candidate names to candidatelist\n",
    "\n",
    "        candidatelist.append(row[2])\n",
    "\n",
    "        #Create a set from the candidatelist to get the unique candidate names\n",
    "\n",
    "    for x in set(candidatelist):\n",
    "\n",
    "        unique_candidate.append(x)\n",
    "\n",
    "        # y is the total number of votes per candidate\n",
    "\n",
    "        y = candidatelist.count(x)\n",
    "\n",
    "        vote_count.append(y)\n",
    "\n",
    "        # z is the percent of total votes per candidate\n",
    "\n",
    "        z = (y/count)*100\n",
    "\n",
    "        vote_percent.append(z)\n",
    "\n",
    "        \n",
    "\n",
    "    winning_vote_count = max(vote_count)\n",
    "\n",
    "    winner = unique_candidate[vote_count.index(winning_vote_count)]\n",
    "\n",
    "    \n",
    "\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"Election Results\")   \n",
    "\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"Total Votes :\" + str(count))    \n",
    "\n",
    "print(\"-------------------------\")\n",
    "\n",
    "for i in range(len(unique_candidate)):\n",
    "\n",
    "            print(unique_candidate[i] + \": \" + str(vote_percent[i]) +\"% (\" + str(vote_count[i])+ \")\")\n",
    "\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"The winner is: \" + winner)\n",
    "\n",
    "print(\"-------------------------\")\n",
    "\n",
    "\n",
    "\n",
    "# Print to a text file: election_results.txt\n",
    "\n",
    "with open('election_results.txt', 'w') as text:\n",
    "\n",
    "    text.write(\"Election Results\\n\")\n",
    "\n",
    "    text.write(\"---------------------------------------\\n\")\n",
    "\n",
    "    text.write(\"Total Vote: \" + str(count) + \"\\n\")\n",
    "\n",
    "    text.write(\"---------------------------------------\\n\")\n",
    "\n",
    "    for i in range(len(set(unique_candidate))):\n",
    "\n",
    "        text.write(unique_candidate[i] + \": \" + str(vote_percent[i]) +\"% (\" + str(vote_count[i]) + \")\\n\")\n",
    "\n",
    "    text.write(\"---------------------------------------\\n\")\n",
    "\n",
    "    text.write(\"The winner is: \" + winner + \"\\n\")\n",
    "\n",
    "    text.write(\"---------------------------------------\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
