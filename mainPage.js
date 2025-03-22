import React from 'react';
import { 
    StyleSheet, 
    View, 
    Text, 
    TouchableOpacity,
    SafeAreaView,
    Image 
} from 'react-native';


const WelcomeScreen = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
                <View style={styles.content}>
                    <Image 
                        source={require('./assets/turist.jpg')}
                        style={styles.logo}
                    />
                    
                    <Text style={styles.title}>LOCAL GUIDE</Text>
                    <Text style={styles.subtitle}>WELCOME TO LOCALGUIDE!</Text>

                    <View style={styles.buttonContainer}>
                        <TouchableOpacity 
                            style={styles.button}
                            onPress={() => navigation.navigate('Login')}
                        >
                            <Text style={styles.buttonText}>Log in</Text>
                        </TouchableOpacity>

                        <TouchableOpacity 
                            style={[styles.button, styles.signupButton]}
                            onPress={() => navigation.navigate('SignUp')}
                        >
                            <Text style={styles.buttonText}>Sign up</Text>
                        </TouchableOpacity>
                    </View>
                </View>
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#5CCBF0',
    },
    content: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
    },
    logo: {
        width: 120,
        height: 120,
        marginBottom: 20,
    },
    title: {
        fontSize: 32,
        fontWeight: 'bold',
        color: 'black',
        marginBottom: 10,
    },
    subtitle: {
        fontSize: 16,
        color: 'black',
        marginBottom: 40,
    },
    buttonContainer: {
        width: '100%',
        paddingHorizontal: 40,
    },
    button: {
        backgroundColor: '#1B2C49',
        padding: 15,
        borderRadius: 25,
        alignItems: 'center',
        marginBottom: 15,
    },
    signupButton: {
        backgroundColor: '#1B2C49',
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: 'bold',
    }
});

export default WelcomeScreen;
