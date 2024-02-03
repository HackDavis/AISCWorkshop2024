from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
# from algorithm import run_algorithm
from main import run_algorithm
from eda import analysis
from flask_restful import Api, Resource

