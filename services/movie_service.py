class MovieService():
        
    def __init__(self, collection) -> None:
        self.collection = collection
    
    def get_movies(self):
        result = self.collection.find({}, {'_id':0}).sort('movie_id')
        return result

    def get_movie_by_id(self, id):
        result = self.collection.find_one({'movie_id': id}, {'_id':0})
        return result
    
    def get_movie_by_params(self, category, year):
        result = self.collection.find({'$and':[{'category': category}, {'year': year}]}, {'_id':0})
        return result
    
    def create_movie(self, movie):
        result = self.collection.insert_one(dict(movie))
        return result

    def update_movie(self, id, movie):
        result = self.collection.update_one({'movie_id': id}, {'$set': dict(movie)})
        return result
    
    def delete_movie(self, id):
        result = self.collection.delete_one({'movie_id': id})
        return result