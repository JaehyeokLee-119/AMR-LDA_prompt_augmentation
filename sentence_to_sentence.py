import os 
# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
# import nltk
# nltk.download('wordnet')

import amrlib
# from amrlib.models.parse_xfm.inference import Inference
import pandas as pd
from tqdm import tqdm 
import logical_equivalence_functions as lef
## Test batch cases
sentence_list = []
logic_word_list = []
dataframe_list = []
dataframe_list_single_sentences = []


class SentenceManipulator:
    def __init__(self, model_path="/hdd/hjl8708/workspace/AMR-LDA/Refactoried/pretrained_models"):
        # sentence -> graph 모델 로드
        self.stog = amrlib.load_stog_model(f"{model_path}/model_parse_xfm_bart_large-v0_1_0")
        self.gtos = amrlib.load_gtos_model(f"{model_path}/model_generate_t5wtense-v0_1_0")
        
    def manipulate(self, sentence):
        sentence_list = [sentence]

        stog = self.stog
        gtos = self.gtos
        
        graphs = stog.parse_sents(sentence_list)
        double_negation_list, double_negation_label_list, double_negation_sentence_and_tag_list = [], [], []
        contraposition_list, contraposition_label_list, contraposition_sentence_and_tag_list = [], [], []
        commutative_list, commutative_label_list, commutative_sentence_and_tag_list = [], [], []
        implication_list, implication_label_list, implication_sentence_and_tag_list = [], [], []
        double_negation_list, double_negation_label_list, double_negation_sentence_and_tag_list = [], [], []

        logic_word_list = [None for _ in range(len(sentence_list))]
        double_negation_list, double_negation_label_list, double_negation_sentence_and_tag_list = lef.double_negation(graphs, gtos, sentence_list, logic_word_list)
        contraposition_list, contraposition_label_list, contraposition_sentence_and_tag_list = lef.contraposition(graphs, sentence_list, logic_word_list)
        commutative_list, commutative_label_list, commutative_sentence_and_tag_list = lef.commutative(graphs, sentence_list, logic_word_list)
        implication_list, implication_label_list, implication_sentence_and_tag_list = lef.implication(graphs, sentence_list, logic_word_list)

        manipulated_graph_lists = double_negation_list + contraposition_list + commutative_list + implication_list
        manipulated_graph_label_list = double_negation_label_list + contraposition_label_list + commutative_label_list + implication_label_list
        
        manipulated_graph_lists_positive = []
        for graph_, label_ in zip(manipulated_graph_lists, manipulated_graph_label_list):
            if label_ == 1:
                manipulated_graph_lists_positive.append(graph_)
        
        # double_negation_generated = gtos.generate(double_negation_list)
        # contraposition_generated = gtos.generate(contraposition_list)
        # commutative_generated = gtos.generate(commutative_list)
        # implication_generated = gtos.generate(implication_list)

        counts_for_types = [len(double_negation_list)>0, len(contraposition_list)>0, len(commutative_list)>0, len(implication_list)>0]
        
        
        
        generated_sentences = gtos.generate(manipulated_graph_lists_positive)
        
        # if True not in counts_for_types:
        #     print("what happened?")
        return generated_sentences[0], counts_for_types
    
    def test(self):
        condition_sentence = "If the wolf is not slow, then the lion is not boring."
        condition_generated, _ = self.manipulate(condition_sentence)
        
        '''
        contraposition_generated = ['The wolf is slow if the lion bores.', "The lion wouldn't be bored if the wolf was slow."]
        implication_generated = ['wolf slow or lion bored.', "The wolf isn't slow or the lion isn't bored."]
        '''
        
        
        judge_sentence = "I am happy."
        judge_generated, _ = self.manipulate(judge_sentence)
        '''
        double_negation_generated = ["I'm not unhappy.", "I'm unhappy."]
        '''
        
        
        print("condition_sentence: ", condition_sentence)
        print("condition_generated: ", condition_generated)
        
        

if __name__ == "__main__":
    sm = SentenceManipulator()
    sm.test()
    