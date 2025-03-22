import React from 'react';
import {
    StyleSheet,
    View,
    Text,
    TextInput,
    TouchableOpacity,
    SafeAreaView,
} from 'react-native';

const VerificationCode = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>Check your email!</Text>
                
                <View style={styles.codeContainer}>
                    <Text style={styles.label}>Enter verification code</Text>
                    <View style={styles.codeInputContainer}>
                        <TextInput style={styles.codeInput} maxLength={1} keyboardType="number-pad" />
                        <TextInput style={styles.codeInput} maxLength={1} keyboardType="number-pad" />
                        <TextInput style={styles.codeInput} maxLength={1} keyboardType="number-pad" />
                        <TextInput style={styles.codeInput} maxLength={1} keyboardType="number-pad" />
                    </View>
                </View>

                <TouchableOpacity 
                    style={styles.button}
                    onPress={() => navigation.navigate('CreateNewPassword')}
                >
                    <Text style={styles.buttonText}>Send</Text>
                </TouchableOpacity>

                <TouchableOpacity>
                    <Text style={styles.resendCode}>Didn't receive a code?</Text>
                    <Text style={styles.resendButton}>Resend</Text>
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
    codeContainer: {
        marginBottom: 30,
    },
    label: {
        color: 'white',
        fontSize: 16,
        marginBottom: 20,
    },
    codeInputContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginBottom: 30,
    },
    codeInput: {
        backgroundColor: '#F5F5F5',
        width: 60,
        height: 60,
        borderRadius: 10,
        textAlign: 'center',
        fontSize: 24,
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
    resendCode: {
        color: 'white',
        textAlign: 'center',
        marginTop: 10,
    },
    resendButton: {
        color: 'white',
        textAlign: 'center',
        fontWeight: 'bold',
        marginTop: 5,
    },
});

export default VerificationCode;