import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(CrossBorderApp());
}

class CrossBorderApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '跨境出海智库',
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: Color(0xFF1A2B3C),
        accentColor: Colors.blueAccent,
        scaffoldBackgroundColor: Color(0xFF0D1B2A),
      ),
      home: HomeScreen(),
    );
  }
}
