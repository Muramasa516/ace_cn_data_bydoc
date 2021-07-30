class Config(object):	
	apr_dir = 'model/'
	data_dir = 'data/'
	model_name = 'model_bert.pt'
	epoch = 3
	bert_model = 'bert_chinese/'
	lr = 3e-5
	eps = 1e-8
	batch_size = 8
	mode = 'train' # for prediction mode = "prediction"
	training_data = "train_data.txt"
	val_data = "dev_data.txt"
	test_data ="test_data.txt"
	test_out = 'test_train_prediction.csv'
	raw_prediction_output = 'raw_prediction.csv'
