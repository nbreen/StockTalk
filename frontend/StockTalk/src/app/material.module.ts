import { NgModule } from  '@angular/core';
 
import { MatButtonModule } from  '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';

import { MatNativeDateModule } from '@angular/material/core';
import { MatIconModule } from '@angular/material/icon';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';
import { MatListModule } from  '@angular/material/list';
import { MatDatepickerModule}  from  '@angular/material/datepicker';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

 
 

@NgModule({
imports: [MatButtonModule,
    MatToolbarModule,
    MatNativeDateModule,
    MatIconModule,
    MatCheckboxModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,
    MatListModule,
    MatDatepickerModule,
    FormsModule,
    ReactiveFormsModule
],
exports: [MatButtonModule,
    MatToolbarModule,
    MatNativeDateModule,
    MatIconModule,
    MatCheckboxModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,
    MatListModule,
    MatDatepickerModule,
    FormsModule,
    ReactiveFormsModule
],
 
})
 
export  class  MyMaterialModule { }