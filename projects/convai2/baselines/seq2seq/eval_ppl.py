# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Evaluate pre-trained model trained for ppl metric.
This seq2seq model was trained on convai2:self.
"""
from parlai.core.build_data import download_models
from projects.convai2.eval_ppl import setup_args, eval_ppl



if __name__ == '__main__':
    parser = setup_args()
    parser.set_params(
        model='parlai.agents.seq2seq.seq2seq:PerplexityEvaluatorAgent',
        model_file='models:convai2/seq2seq/convai2_self_seq2seq_model',
        dict_file='models:convai2/seq2seq/convai2_self_seq2seq_model.dict',
        dict_lower=True,
        batchsize=1,
        numthreads=60,
        no_cuda=True,
    )
    opt = parser.parse_args()
    if opt.get('model_file', '').find('convai2/seq2seq/convai2_self_seq2seq_model') != -1:
        opt['model_type'] = 'seq2seq'
        fnames = ['convai2_self_seq2seq_model.tgz',
                  'convai2_self_seq2seq_model.dict',
                  'convai2_self_seq2seq_model.opt']
        download_models(opt, fnames, 'convai2', version='v3.0')
    eval_ppl(opt)
