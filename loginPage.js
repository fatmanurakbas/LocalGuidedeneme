import React from 'react';
import {
    StyleSheet,
    View,
    Text,
    TextInput,
    TouchableOpacity,
    SafeAreaView,
} from 'react-native';

const Login = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.content}>
                <Text style={styles.title}>Welcome back!</Text>
                
                <View style={styles.inputContainer}>
                    <Text style={styles.label}>Email</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                        keyboardType="email-address"
                    />
                    
                    <Text style={styles.label}>Password</Text>
                    <TextInput
                        style={styles.input}
                        placeholder=""
                        secureTextEntry
                    />
                    
                    <TouchableOpacity onPress={() => navigation.navigate('ForgotPassword')}>
                        <Text style={styles.forgotPassword}>Forgot password?</Text>
                    </TouchableOpacity>
                </View>

                <TouchableOpacity style={styles.button}>
                    <Text style={styles.buttonText}>Log in</Text>
                </TouchableOpacity>

                <View style={styles.footer}>
                    <Text style={styles.footerText}>Don't have an account?</Text>
                    <TouchableOpacity onPress={() => navigation.navigate('SignUp')}>
                        <Text style={styles.signupText}>Sign up</Text>
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
    forgotPassword: {
        color: 'white',
        textAlign: 'right',
        marginTop: -10,
        marginBottom: 20,
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
    footer: {
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
    },
    footerText: {
        color: 'white',
        marginRight: 5,
    },
    signupText: {
        color: 'white',
        fontWeight: 'bold',
    },
});

export default Login;