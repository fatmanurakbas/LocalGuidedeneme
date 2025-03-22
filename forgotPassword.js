import React from 'react';
import {
    StyleSheet,
    View,
    Text,
    TextInput,
    TouchableOpacity,
    SafeAreaView,
} from 'react-native';

const ForgotPassword = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>Forgot password?</Text>
                
                <View style={styles.inputContainer}>
                    <Text style={styles.label}>Enter Email Address</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                        keyboardType="email-address"
                    />
                </View>

                <TouchableOpacity 
                    style={styles.button}
                    onPress={() => navigation.navigate('Verification')}
                >
                    <Text style={styles.buttonText}>Send</Text>
                </TouchableOpacity>

                <TouchableOpacity onPress={() => navigation.navigate('Login')}>
                    <Text style={styles.backToLogin}>Back to log in</Text>
                </TouchableOpacity>
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
        padding: 20,
        paddingTop: 60,
    },
    title: {
        fontSize: 32,
        color: 'white',
        marginBottom: 40,
    },
    inputContainer: {
        marginBottom: 30,
    },
    label: {
        color: 'white',
        fontSize: 16,
        marginBottom: 8,
    },
    input: {
        backgroundColor: '#F5F5F5',
        borderRadius: 10,
        padding: 15,
        marginBottom: 20,
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    button: {
        backgroundColor: '#1B2C49',
        padding: 15,
        borderRadius: 25,
        alignItems: 'center',
        marginBottom: 20,
        shadowColor: '#000',
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: 'bold',
    },
    backToLogin: {
        color: 'white',
        textAlign: 'center',
        marginTop: 10,
    },
});

export default ForgotPassword;