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
        scaffoldBackgroundColor: Color(0xFF020B18), // Deeper dark blue
        cardTheme: CardTheme(
          color: Colors.white.withOpacity(0.05),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          elevation: 0,
        ),
        appBarTheme: AppBarTheme(
          backgroundColor: Colors.transparent,
          elevation: 0,
          centerTitle: true,
          titleTextStyle: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
        ),
      ),
      home: HomeScreen(),
    );
  }
}
