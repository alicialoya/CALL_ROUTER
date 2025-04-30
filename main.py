from model_utils import prepare_training_data, predict
from record_audio import record_audio

def route_call(predicted_keyword):
    routes = {
        'Sales': 'Routing to Sales Department...',
        'Support': 'Routing to Support Department...',
        'Billing': 'Routing to Billing Department...'
    }
    return routes.get(predicted_keyword, "Keyword not recognized. Please try again.")

if __name__ == "__main__":
    print("Preparing training data...")
    models = prepare_training_data('dataset')

    print("\nWould you like to record a new call or use an existing file?")
    choice = input("Enter 'record' to record new or 'file' to use existing: ").strip()

    if choice == 'record':
        record_audio('test.wav')
        test_file = 'test.wav'
    else:
        test_file = input("Enter path to .wav file: ").strip()

    predicted_keyword = predict(models, test_file)
    print(f"Predicted Keyword: {predicted_keyword}")

    routing_message = route_call(predicted_keyword)
    print(routing_message)
